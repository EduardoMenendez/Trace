<script>
  // @ts-nocheck
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import { page } from '$app/stores';
  import { get } from 'svelte/store';

  let treeData = null;
  let treeContainer;

  const projectId = $page.params.project_id;
  const host = $page.params.host;

  onMount(async () => {
    try {
      const res = await fetch(`http://localhost:8000/projects/${projectId}/outputs/${host}/tree`);
      if (!res.ok) throw new Error("Failed to fetch tree data");
      treeData = await res.json();

      drawTree(treeData);
    } catch (err) {
      console.error("Error loading tree data:", err);
    }
  });

  function drawTree(treeData) {
    const width = 800, height = 500;

    const svg = d3.select(treeContainer)
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", "translate(40,40)");

    const treeLayout = d3.tree().size([width - 100, height - 100]);

    const root = d3.hierarchy(treeData, d => d.children);
    treeLayout(root);

    svg.selectAll("line")
      .data(root.links())
      .enter()
      .append("line")
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y + 20) 
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y - 20)
      .attr("stroke", "#ccc");

    const nodeGroup = svg.selectAll(".node")
      .data(root.descendants())
      .enter()
      .append("g")
      .attr("class", "node")
      .attr("transform", d => `translate(${d.x - 75}, ${d.y - 30})`);

    nodeGroup.append("rect")
      .attr("width", 150)
      .attr("height", 60)
      .attr("fill", "#E3E3E3")
      .attr("stroke", "#000")
      .attr("rx", 5)
      .attr("ry", 5);

    nodeGroup.append("text")
      .attr("x", 75)
      .attr("y", 20)
      .attr("text-anchor", "middle")
      .style("font-size", "10px")
      .style("fill", "#555")
      .text(d => d.data.node_id);

    nodeGroup.append("text")
      .attr("x", 75)
      .attr("y", 35)
      .attr("text-anchor", "middle")
      .style("font-size", "12px")
      .style("font-weight", "bold")
      .style("fill", "#000")
      .text(d => d.data.name);

    nodeGroup.append("text")
      .attr("x", 75)
      .attr("y", 50)
      .attr("text-anchor", "middle")
      .style("font-size", "10px")
      .style("fill", d => {
        if (d.data.severity === "High") return "red";
        if (d.data.severity === "Medium") return "orange";
        return "green";
      })
      .text(d => `Severity: ${d.data.severity}`);
  }
</script>

<div bind:this={treeContainer}></div>

<div class="container">
  
  <h1>Tree Graph</h1>
  
  <div bind:this={treeContainer} class="tree-container"></div>

</div>

<style>
  .container{
        padding: 50px;
        width: 100%;
    }
  .tree-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
    body {
    margin: 0;
    padding: 0;
    overflow: hidden; /* avoid scroll */
  }

  /* Tree container */
  .tree-container {
    margin: 0;
    padding: 0;
  }
</style>
