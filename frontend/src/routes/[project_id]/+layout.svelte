<script>
    import '../css/global.css';
    let {children} = $props();
    import Nav from '$lib/components/nav.svelte';
    import { page } from '$app/stores';
    const id = $page.params.project_id;
</script>
<div class="container">
    <Nav type="tools" id={id}/>
    {@render children()}
</div>
<style>
    .container{
        display: flex;
        gap: 30px;
    }
</style>