<script lang="ts">
    import './css/global.css';
</script>
<nav>
    <img src="/img/logo.png" alt="logo" class="logo">
    <div class="nav-options">
        <a href="/dashboard">Dashboard</a>
        <a href="/dashboard/settings">Settings</a>
    </div>
</nav>
<div class="container">
    <h1>Elevate Your Security <br/>Strategy with TRACE</h1>
    <p>A Cybersecurity Platform to Protect Digital Assets. Detect <br/>Vunerabilities, Strengthen Defense, and Secure Your Network Seamlessly. <br/>Gain Real-Time insights and Proactive Protection.</p>
    <a href="/auth" class="button">Start</a>
</div>

<style>
    nav{
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 40px;
    align-items: center;
    height: 8vh;
}
.nav-options{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.nav-options>a{
    color: gray;
    text-decoration: none;
    font-size: 15px;
    margin-inline: 20px;
    font-weight: 500;
}
.container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 85vh;
    gap: 50px;
    background-image: url('./img/bg.svg');
    background-repeat: no-repeat;
    background-size: cover;
}
.container>h1{
    font-size: 4rem;
    text-align: center;
    background: none;
}
.container>p{
    font-size: 1.2rem;
    text-align: center;
    background: none;
    word-break: initial;
}
.button{
    text-decoration: none;
    color: white;
    text-transform: uppercase;
    background-color: #4aa6b0;
    padding: 15px 25px;
    border-radius: 10px;
    letter-spacing: 3px;
}
</style>