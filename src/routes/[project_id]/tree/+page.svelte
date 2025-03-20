<script>
    import { goto } from '$app/navigation';
    const sites = [
        {parent: '192.168.1.25:8080', severity: 'Medium'},
        {parent: '192.168.3.27:8080', severity: 'Medium'},
        {parent: '192.168.2.26:8080', severity: 'Low'},
        {parent: '192.168.4.28:8080', severity: 'Low'},
        {parent: '192.168.5.29:8080', severity: 'High'},
        {parent: '192.168.6.30:8080', severity: 'Medium'},
    ]
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
            <button class="primary-button" onclick={()=>{goto('tree/WebTree')}}>View</button>
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