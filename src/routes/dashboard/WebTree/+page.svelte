<script>
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

    // Convertir `treeData` en una jerarquía
    const root = d3.hierarchy(treeData, d => d.children);
    treeLayout(root);

    // Dibujar las líneas (links)
    svg.selectAll("line")
      .data(root.links())
      .enter()
      .append("line")
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y + 20) // Ajustar para conectar con el rectángulo
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y - 20) // Ajustar para conectar con el rectángulo
      .attr("stroke", "#ccc");

    // Crear nodos con rectángulos
    const nodeGroup = svg.selectAll(".node")
      .data(root.descendants())
      .enter()
      .append("g")
      .attr("class", "node")
      .attr("transform", d => `translate(${d.x - 75}, ${d.y - 30})`);

    // Rectángulo de cada nodo
    nodeGroup.append("rect")
      .attr("width", 150)
      .attr("height", 60)
      .attr("fill", "#E3E3E3")
      .attr("stroke", "#000")
      .attr("rx", 5)
      .attr("ry", 5);

    // Primera línea: Mostrar el ID (node_id)
    nodeGroup.append("text")
      .attr("x", 75)
      .attr("y", 20)
      .attr("text-anchor", "middle")
      .style("font-size", "10px")
      .style("fill", "#555")
      .text(d => d.data.node_id);

    // Segunda línea: Mostrar el Nombre
    nodeGroup.append("text")
      .attr("x", 75)
      .attr("y", 35)
      .attr("text-anchor", "middle")
      .style("font-size", "12px")
      .style("font-weight", "bold")
      .style("fill", "#000")
      .text(d => d.data.name);

    // Tercera línea: Mostrar el Severity con color
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

<div bind:this={treeContainer} class="tree-container"></div>

<style>
  .tree-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
