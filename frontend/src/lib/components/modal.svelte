<script>
	let { showModal = $bindable(), header, children } = $props();

	let dialog = $state();

	$effect(() => {
		if (showModal) {
			dialog.showModal();
			document.body.classList.add('no-scroll');
		} else {
			document.body.classList.remove('no-scroll');
		}
	});
</script>


<dialog
	bind:this={dialog}
	onclose={() => (showModal = false)}
	onclick={(e) => { if (e.target === dialog) dialog.close(); }}
>
	<div>
		<div class="flex">
			{@render header?.()}
			<button autofocus onclick={() => dialog.close()}>X</button>
		</div>
		{@render children?.()} 
	</div>
</dialog>

<style>
	dialog {
		border-radius: 0.2em;
		border: none;
		padding: 0;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		padding: 20px;
		border-radius: 20px;
		min-width: 40vw;
	}
	dialog::backdrop {
		background: rgba(0, 0, 0, 0.3);
	}
	dialog > div {
		padding: 1em;
	}
	button{
		border: none;
		font-size: 1.2em;
		color: #969696;
		cursor: pointer;
	}
	dialog[open]::backdrop {
		animation: fade 0.2s ease-out;
	}
	.flex{
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding-bottom: 30px;
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}
	:global(.no-scroll) {
		overflow: hidden;
	}
</style>
