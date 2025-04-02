import subprocess
import json
import urllib.parse
from typing import List

class Node:
    def __init__(self, node_id: str, name: str, severity: str, children: list = None):
        self.node_id = node_id
        self.name = name
        self.severity = severity
        self.children = children if children is not None else []

    def add_child(self, child: 'Node'):
        """Add a child node."""
        self.children.append(child)

    def to_dict(self) -> dict:
        """Recursively convert the Node (and its children) into a dictionary."""
        return {
            "node_id": self.node_id,
            "name": self.name,
            "severity": self.severity,
            "children": [child.to_dict() for child in self.children]
        }

    def __repr__(self):
        return f"Node(node_id={self.node_id!r}, name={self.name!r}, severity={self.severity!r}, children={self.children!r})"

def get_severity(status_code: int) -> str:
    """
    A simple mapping from HTTP status code to severity.
    """
    if status_code == 200:
        return "High"
    elif status_code == 403:
        return "Medium"
    else:
        return "Low"


def insert_url_into_tree(root: Node, url: str, severity: str):
    """
    Inserts the URL into the tree by splitting its path into segments.
    The root node is expected to match the base URL (scheme + netloc).
    """
    parsed = urllib.parse.urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    if root.node_id != base:
        print(f"Warning: URL {url} does not match the root base {root.node_id}. Skipping insertion.")
        return
    
    # Split the path into segments (ignoring empty segments)
    segments = [seg for seg in parsed.path.split("/") if seg]
    current_node = root
    current_url = base
    for seg in segments:
        current_url += f"/{seg}"
        # Check if a child node with this segment already exists
        found = next((child for child in current_node.children if child.name == seg), None)
        if not found:
            # Create a new node with a default severity; it will be updated at the leaf.
            new_node = Node(node_id=current_url, name=seg, severity="Low")
            current_node.add_child(new_node)
            current_node = new_node
        else:
            current_node = found
    # Update the severity at the final node
    current_node.severity = severity


def run_wfuzz_and_build_tree(
    target_url: str,
    wordlist: str,
    user_agent: str = None,
    proxy: str = None,
    delay: float = 0
) -> Node:
    """
    Runs wfuzz using subprocess with JSON output, parses the results,
    and builds a Node tree.
    
    Args:
        target_url (str): The target URL with the 'FUZZ' placeholder.
        wordlist (str): Path to the wordlist file.
        user_agent (str): Custom User-Agent header.
        proxy (str): Proxy address (host:port).
        delay (float): Delay between requests in seconds.
    
    Returns:
        Node: The root of the resulting tree.
    """
    # Build the wfuzz command line
    command = [
        "wfuzz",
        "-w", wordlist, 
        "-o", "json" 
    ]
    if user_agent:
        command += ["-H", f"\"User-Agent: {user_agent}\""]
    if proxy:
        command += ["-p", proxy]
    if delay:
        command += ["-s", str(delay)]
    
    command.append(target_url)

    # print(f"[*] Running wfuzz command: {' '.join(command)}")
    process = subprocess.run(command, capture_output=True, text=True)
    
    if process.returncode != 0:
        print("[!] Wfuzz error:", process.stderr)
        return None
    
    try:
        results = json.loads(process.stdout)
    except json.JSONDecodeError as e:
        print("[!] Failed to parse JSON output from wfuzz:", e)
        return None
    
    # Create a root node based on the target URL (without the FUZZ part)
    parsed_target = urllib.parse.urlparse(target_url.replace("FUZZ", ""))
    base_url = f"{parsed_target.scheme}://{parsed_target.netloc}"
    root = Node(node_id=base_url, name=parsed_target.netloc, severity="Low")
    
    # Process each result: assume each result has 'url' and 'status_code'
    for result in results:
        url = result.get("url")
        status_code = result.get("code")
        if url is None or status_code is None:
            continue
        severity = get_severity(status_code)
        insert_url_into_tree(root, url, severity)
    
    return root


def main():
    target_url = "http://localhost:5173/FUZZ"
    wordlist = "../dictionaries/common.txt"
    user_agent = "Mozilla/5.0"
    proxy = "127.0.0.1:8080"
    delay = 1  # Delay in seconds
    
    tree = run_wfuzz_and_build_tree(target_url, wordlist, user_agent, proxy, delay)
    if tree:
        # Print the resulting tree as a dictionary for visualization
        import json
        print(tree.to_dict())


if __name__ == "__main__":
    main()
