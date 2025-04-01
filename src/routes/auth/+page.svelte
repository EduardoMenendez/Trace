<script>
    import '../css/global.css';
    import { goto } from '$app/navigation';

    let role = '';
    let initials = '';
    let errorMessage = '';

    const acceptedRoles = ['LEAD', 'ANALYST'];

    $: trimmedInitials = initials.trim().toUpperCase();
    $: isRoleValid = acceptedRoles.includes(role);
    $: isInitialsValid = /^[A-Z]{2,3}$/.test(trimmedInitials);
    $: isFormValid = isRoleValid && isInitialsValid;

    const handleSubmit = (event) => {
        event.preventDefault();
        if (!isFormValid) {
            errorMessage = 'Please select a valid role and provide valid initials.';
            return;
        }
        errorMessage = '';
        initials = trimmedInitials;
        goto('/dashboard');
    };
</script>

<div class="container">
    <div class="card">
        <h1>TRACE</h1>
        <form on:submit={handleSubmit}>
            <label for="role">Role</label>
            <select id="role" bind:value={role}>
                <option value="">Select a role</option>
                <option value="LEAD">Lead</option>
                <option value="ANALYST">Analyst</option>
            </select>

            <label for="initials">Initials</label>
            <input
                type="text"
                id="initials"
                bind:value={initials}
                placeholder="e.g. AP"
                on:input={() => {
                    initials = initials.toUpperCase();
                }}
            />

            <button type="submit" disabled={!isFormValid}>Sign In</button>
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

    select, input {
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

    button:disabled {
        background-color: #666;
        cursor: not-allowed;
    }

    button:hover:enabled {
        background-color: #333;
    }

    .error {
        color: red;
        font-size: 12px;
        margin-top: 10px;
    }
</style>
