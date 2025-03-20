<script>
    import { page } from '$app/stores';
    import {projects} from '$lib/data/projects';
    
    const project = projects.find((value)=>value.id===$page.params.project_id);
    console.log(project);
</script>
<div class="container">
    <h1>Tools</h1>
    <h3>{project?.title}</h3>
</div>

<style>
    .container{
        padding: 50px;
        width: 100%;
    }
    h1{
        font-size: 2.5em;
        font-weight: 600;
    }
</style>