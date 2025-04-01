<script>
    import { user } from '$lib/stores/user';
    import {folders} from '$lib/data/folders';  
    import Alert from '$lib/components/Alert.svelte';
    console.log($user);

    const recents = [
        {title: "Recon Week 6", date: "Nov 7, 2024"},
        {title: "High Security 3", date: "Nov 6, 2024"},
        {title: "Critical Data Test", date: "Nov 5, 2024"},
        {title: "Remote Access Test", date: "Nov 4, 2024"},
    ];
    // Function to handle the creation of a new project 
    let showModal = false;
    let alertMessage = "";
    let showAlert = false;
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
        <h1>Project Folders</h1>
        <div class="button-holder">
            <!-- <button class="primary-button">+ Create New</button> -->
            <button class="primary-button" onclick={handleCreateProject}>+ Create New</button>
            <button class="secondary-button" style="padding: 4px 10px;"><img src="/img/import.svg" alt="" style="background:none;"></button>
        </div>
    </div>
     <!-- alert component -->
     <Alert message={alertMessage} visible={showAlert} onDismiss={dismissAlert} />
    <h2>Recent Folders</h2>
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
    <div class="space-between">
        <h2>All Folders</h2>
        
        <div class="button-holder" style="display: flex; align-items: center; justify-content: center;">
            <input type="text" class="icon" placeholder="Search...">
            <button style="border: none; background: none; cursor:pointer; padding: 10px"><img src="/img/filter.svg" alt="" class="icon-img"></button>
        </div>
    </div>

    <div class="folders">
        {#each folders as folder}
            <div class="card">
                <div class="title-card">
                    <h4>{folder.title}</h4>
                    <p class="mute">{folder.date}</p>
                </div>
                <div class="bottom-card">
                    <p>{folder.creator}</p>
                    <button style="background: none; border: none"><img src="/img/options.svg" alt="" style="width: 20px; background: none;"></button>
                </div>
            </div>
        {/each}
    </div>
</div>

<style>
    .folders{
        display: flex;
        flex-wrap: wrap;
        gap: 50px;
    }
    .card{
        width: 350px;
        background-color: #e1e1e1;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 40px;
        border-radius: 10px;
    }
    .title-card, .bottom-card, h4, p{
        background: none;
    }
    .bottom-card{
        display: flex;
        justify-content: space-between;
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
</style>