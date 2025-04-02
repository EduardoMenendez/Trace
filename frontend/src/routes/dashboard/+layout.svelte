<script>
    import '../css/global.css';
    let {children} = $props();
    import Nav from '$lib/components/nav.svelte';
</script>
<div class="container">
    <Nav type="dashboard"/>
    {@render children()}
</div>
<style>
    .container{
        display: flex;
        gap: 30px;
    }
</style>