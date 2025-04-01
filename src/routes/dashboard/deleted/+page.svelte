<script>
    import {projects} from '$lib/data/projects';
    import { user } from '$lib/stores/user';
    console.log($user);

</script>
<div class="container">
    <h1>Deleted Projects</h1>
    <div class="button-holder">
        <input type="text" class="icon" placeholder="Search...">
        <button style="border: none; background: none; cursor:pointer; padding: 10px"><img src="/img/filter.svg" alt="" class="icon-img"></button>
    </div>
    {#each projects as project}
                <div class="project">
                    <p style="text-align: left;">{project.title}</p>
                    <p>{project.last_edit}</p>
                    <p>{project.lead}</p>
                    <button style="background: none; border: none"><img src="/img/options.svg" alt="" style="width: 20px; background: none;"></button>
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
</style>