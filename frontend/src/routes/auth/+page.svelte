<script>
    import '../css/global.css';
    import { goto } from '$app/navigation'; // Import for SvelteKit navigation
    import { user } from '$lib/stores/user';

    let role = '';
    let initials = '';
    let errorMessage = '';

    // Define the accepted roles
    const acceptedRoles = ['LEAD', 'ANALYST'];

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log("Form submitted!");  // Debugging log

        const trimmedRole = role.trim().toUpperCase();
        // Validate the role
        if (!acceptedRoles.includes(trimmedRole)) {
            errorMessage = 'Invalid role. Please enter again.';
            console.log("Validation failed!");  // Debugging log
            return;
        }
        // Clear any previous error messages
        errorMessage = '';
        // update the user store with the role and initials
        user.set({ role: trimmedRole, initials });
        // Proceed with form submission logic
        console.log("Validation passed!"); 
        console.log("Role:", trimmedRole);
        console.log("Initials:", initials);
        goto('/dashboard'); 
    };
    
</script>

<div class="container">
    <div class="card">
        <h1>TRACE</h1>
        <form on:submit={handleSubmit}>
            <label for="role">Role</label>
            <input type="text" id="role" bind:value={role} placeholder="role...">
            <label for="initials">Initials</label>
            <input type="text" id="initials" bind:value={initials} placeholder="e.g. AP">
            <button type="submit">Sign In</button>
            {#if errorMessage}
                <p class="error">{errorMessage}</p>
            {/if}
        </form>
    </div>
</div>

<style>

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        background-image: url('../img/bg.svg');
        background-repeat: no-repeat;
        background-size: cover;
        height: 100vh;
    
    }

    .card {
        background-color: #eef0f3;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        width: 300px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    h1 {
        margin-bottom: 20px;
        font-size: 24px;
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    label {
        text-align: left;
        font-size: 14px;
        font-weight: bold;
    }

    input {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 14px;
    }

    button {
        background-color: black;
        color: white;
        border: none;
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 10px;
    }

    button:hover {
        background-color: #333;
    }
</style>
