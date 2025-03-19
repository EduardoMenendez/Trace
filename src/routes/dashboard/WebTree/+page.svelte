<script>
  // @ts-nocheck
  import { onMount } from "svelte";
  import * as d3 from "d3";
  import { treeData } from "$lib/data/treeData.js";

  let treeContainer;

  onMount(() => {
    const width = 800, height = 500;

    const svg = d3.select(treeContainer)
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", "translate(40,40)");

    const treeLayout = d3.tree().size([width - 100, height - 100]);

    // convert the flat data into a hierarchy
    const root = d3.hierarchy(treeData, d => d.children);
    treeLayout(root);

    // Draw links
    svg.selectAll("line")
      .data(root.links())
      .enter()
      .append("line")
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y + 20) 
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y - 20)
      .attr("stroke", "#ccc");

    // draw nodes
    const nodeGroup = svg.selectAll(".node")
      .data(root.descendants())
      .enter()
      .append("g")
      .attr("class", "node")
      .attr("transform", d => `translate(${d.x - 75}, ${d.y - 30})`);

    // each node is a group with a rectangle and text
    nodeGroup.append("rect")
      .attr("width", 150)
      .attr("height", 60)
      .attr("fill", "#E3E3E3")
      .attr("stroke", "#000")
      .attr("rx", 5)
      .attr("ry", 5);

    //  ID (node_id)
    nodeGroup.append("text")
      .attr("x", 75)
      .attr("y", 20)
      .attr("text-anchor", "middle")
      .style("font-size", "10px")
      .style("fill", "#555")
      .text(d => d.data.node_id);

    // Name
    nodeGroup.append("text")
      .attr("x", 75)
      .attr("y", 35)
      .attr("text-anchor", "middle")
      .style("font-size", "12px")
      .style("font-weight", "bold")
      .style("fill", "#000")
      .text(d => d.data.name);

    // Severity 
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
  });
</script>

<h1>Tree Graph</h1>

<div bind:this={treeContainer} class="tree-container"></div>

<style>
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
    width: 100vw;       
    height: 100vh;     
    overflow: hidden;   
    margin: 0;
    padding: 0;
  }
</style>
