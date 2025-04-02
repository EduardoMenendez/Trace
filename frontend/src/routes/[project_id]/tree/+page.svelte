<script>
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    let sites = [];
    const projectId =  $page.params.project_id; 

    onMount(async () => {
        try {
            // console.log(`http://172.21.0.3:8000/projects/${projectId}/crawls`);
            const res = await fetch(`http://localhost:8000/projects/${projectId}/crawls`);
            if (!res.ok) throw new Error("Failed to fetch sites");
            const data = await res.json();

            // Optional: Set a default severity if missing
            sites = data.targets.map(target => ({
                parent: target.host.replace(/_/g, ":"),
                severity: target.severity ?? "Low",
                host: target.host
            }));
        } catch (err) {
            console.error("Error loading sites:", err);
        }
    });

    function viewTree(site) {
        goto(`tree/WebTree/${site.host.replace(":", /_/)}`);
    }
</script>
<div class="container">
    <h1>Tree Graph</h1>
    <div class="button-holder">
        <input type="text" class="icon" placeholder="Search...">
        <button style="border: none; background: none; cursor:pointer; padding: 10px"><img src="/img/filter.svg" alt="" class="icon-img"></button>
    </div>
    {#each sites as site}
        <div class="project">
            <div class={"holder "+site.severity}></div>
            <p style="text-align: left; padding-left: 20px;">{site.parent}</p>
            <p style="text-align: left;">{site.severity}</p>
            <button class="primary-button" on:click={() => viewTree(site)}>View</button>
        </div>
    {/each}
</div>

<style>
    button{
        cursor: pointer;
    }
    .container{
        padding: 50px;
        width: 100%;
    }
    .icon {
        padding-left: 25px;
        background: url("https://static.thenounproject.com/png/3549244-512.png") no-repeat left;
        background-size: 20px;
        padding-block: 10px;
        border-radius: 5px;
        border: none;
        background-color: #e1e1e1;
        transition: 0.2s ease-in-out all;
        width: 500px;
    }
    .icon:focus{
        background-position: -10000px;
        padding: 10px;
        transition: 0.2s ease-in-out all;
    }
    .icon-img{
        height: 30px;
        background: none;
    }
    h1{
        font-size: 2.5em;
        font-weight: 600;
    }
    .space-between{
        display: flex;
        justify-content: space-between;
        width: 100%;
        padding-block: 40px;
    }
    .button-holder{
        display: flex; 
        align-items: center;
        gap: 10px;
        background: none;
        padding-block: 40px;
    }
    .project{
        display: flex;
        width: 100%;
        justify-content: space-between;
        align-items: center;
        padding: 15px;
        margin-bottom: 10px;
        background-color: #e1e1e1;
        border-radius: 5px;
        position: relative;
    }
    .project:hover{
        background-color: #c4c4c4;
    }
    .project>p{
        text-align: center;
        width: 20%;
        background: none;
        font-weight: bold;
    }
    .holder{
        position: absolute;
        left: 10px;
        height: 80%;
        width: 10px;
        border-radius: 10px;
        background-color: #363a44;
    }
    .Low{
        background-color: #2ca85c;
    }
    .High{
        background-color: #db3446;
    }
    .Medium{
        background-color: #db8732;
    }
    .primary-button{
        color: white;
        background-color: #4aa6b0;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
</style>