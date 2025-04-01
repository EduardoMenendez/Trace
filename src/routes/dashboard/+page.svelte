<script>
    import {projects, shared} from '$lib/data/projects';
    import { goto } from '$app/navigation';
    import Modal from '$lib/components/modal.svelte';
    import { user } from '$lib/stores/user';
    import Alert from '$lib/components/Alert.svelte';

    
    console.log($user);

    const recents = [
        {title: "Base Perimeter Network", date: "Nov 7, 2024"},
        {title: "Mission Control Portal", date: "Nov 6, 2024"},
        {title: "Field Operations", date: "Nov 5, 2024"},
        {title: "Government Defense", date: "Nov 4, 2024"},
    ];
    let active = "My Projects";
    let showModal = false;
    let alertMessage = "";
    let showAlert = false;
    /*
   * @param {string} option
   */
    function updateState(option) {
        active = option;
    }
    // Function to handle the creation of a new project 
    function handleCreateProject() {
        if ($user.role === 'LEAD') {
            showModal = true;
        } else {
            alertMessage = "As an Analyst, you cannot perform this task";
            showAlert = true;
        }
    }
    function dismissAlert() {
      showAlert = false;
    }
</script>
<div class="container">
    <div class="space-between">
        <h1>Project Selection</h1>
        <div class="button-holder">
            <!-- <button class="primary-button" onclick={() => (showModal = true)}>+ Create New</button> -->
            <button class="primary-button" onclick={handleCreateProject}>+ Create New</button>
            <button class="secondary-button" style="padding: 4px 10px;"><img src="/img/import.svg" alt="" style="background:none;"></button>
        </div>
    </div>
    <!-- alert component -->
    <Alert message={alertMessage} visible={showAlert} onDismiss={dismissAlert} />

    <h2>Recent Projects</h2>
    <div class="recent">
        {#each recents as recent}
            <div class="recent-item">
                <img src="/img/folder.svg" alt="project logo">
                <div class="text">
                    <h5>{recent.title}</h5>
                    <p class="mute">{recent.date}</p>
                </div>
            </div>
        {/each}
    </div>
    <h2 style="margin-top: 20px;">All Projects</h2>
    <div class="space-between">
        <div class="button-holder">
            <button class={active==="My Projects"?"menu-option active":"menu-option"} onclick={() => updateState('My Projects')}>My Projects</button>
            <button class={active==="Shared"?"menu-option active":"menu-option"} onclick={() => updateState('Shared')}>Shared Projects</button>
        </div>
        <div class="button-holder" style="display: flex; align-items: center; justify-content: center;">
            <input type="text" class="icon" placeholder="Search...">
            <button style="border: none; background: none; cursor:pointer; padding: 10px"><img src="/img/filter.svg" alt="" class="icon-img"></button>
        </div>
    </div>
    <div class="projects">
        {#if active==='My Projects'}
            {#each projects as project}
                <div class="project">
                    <div class={"holder "+project.status}></div>
                    <p style="text-align: left; padding-left: 20px;">{project.title}</p>
                    <p>{project.last_edit}</p>
                    <p>{project.lead}</p>
                    <div class="button-holder">
                        <button class="primary-button" onclick={()=>{goto(`/${project.id}/tools`)}}>Run Scan</button>
                        <button class="secondary-button" style="background: none;"><img src="/img/options.svg" alt="" style="width: 20px; background: none;"></button>
                    </div>
                </div>
            {/each}
        {/if}
        {#if active==='Shared'}
            {#each shared as shared_project}
                <div class="project">
                    <div class={"holder "+shared_project.status}></div>
                    <p style="text-align: left; padding-left: 20px;">{shared_project.title}</p>
                    <p>{shared_project.last_edit}</p>
                    <p>{shared_project.lead}</p>
                    <p>{shared_project.port}</p>
                    <button class="primary-button">Join</button>
                </div>
            {/each}
        {/if}
    </div>
</div>
<Modal bind:showModal>
	{#snippet header()}
		<h2>Create Project</h2>
	{/snippet}

	<div class="cols">
        <div class="half">
            <label for="name">Project Name</label>
            <input type="text" id="name" name="name">
            <div class="cols">
                <div class="half">
                    <label for="date">Start Date</label>
                    <input type="date">
                </div>
                <div class="half">
                    <label for="time">Time:</label>
                    <input type="time">
                </div>
            </div>
            <div class="cols">
                <div class="half">
                    <label for="analyst">Analyst Initials</label>
                    <input type="text" placeholder="e.g. E.M.">
                </div>
            </div>
            <label for="desc">Project Description</label>
            <textarea name="desc" id="desc" rows="20"></textarea>
        </div>
        <div class="half">
            <div class="button-holder" style="width: 100%; justify-content: space-between;">
                <p>Upload NMap</p>
                <button class="secondary-button">Select Files</button>
            </div>
        </div>
    </div>
</Modal>
<style>
    .cols{
        display: flex;
        width: 100%;
        gap: 40px;
    }
    label{
        color: gray;
    }
    .half{
        width: 50%;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    textarea, .half>input[type="text"], input[type="date"], input[type="time"]{
        border-radius: 5px;
        padding: 10px;
        width: 100%;
    }
    button{
        cursor: pointer;
    }
    .button-holder{
        display: flex; 
        align-items: center; 
        justify-content: center;
        gap: 10px;
        background: none;
    }
    .holder{
        position: absolute;
        left: 10px;
        height: 80%;
        width: 10px;
        border-radius: 10px;
        background-color: #363a44;
    }
    .Active{
        background-color: #2ca85c;
    }
    .error{
        background-color: #db3446;
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
    .icon {
        padding-left: 25px;
        background: url("https://static.thenounproject.com/png/3549244-512.png") no-repeat left;
        background-size: 20px;
        padding-block: 10px;
        border-radius: 5px;
        border: none;
        background-color: #e1e1e1;
        transition: 0.2s ease-in-out all;
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
    .container{
        padding: 50px;
        width: 100%;
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
    .recent{
        display: flex;
        padding-block: 20px;
        gap: 40px;
        flex-wrap: wrap;
    }
    .recent-item{
        display: flex;
        align-items: center;
        width: 250px;
        border: 2px solid black;
        border-radius: 10px;
        padding: 20px;
        gap: 10px;
    }
    .recent-item>img{
        width: 40px;
    }
    .mute{
        font-size: 0.7em;
        color: gray;
    }
    .primary-button{
        color: white;
        background-color: #4aa6b0;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
    .secondary-button{
        color: white;
        background-color: #363a44;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    button{
        transition: 0.2s ease-in-out all;
    }
    button:hover{
        transform: scale(1.1);
        transition: 0.2s ease-in-out all;
    }
    .menu-option{
        border: none;
        padding: 5px 0px;
        margin-inline: 10px;
        font-size: 1.05em;
        cursor: pointer;
    }
    .active{
        border-bottom: 4px solid #74b9c1;
    }
</style>