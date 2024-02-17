<script>
	import Button, { Label } from '@smui/button';
	let clicked = 0;
</script>

<main>
	<h1>Hello {clicked}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<Button on:click={() => clicked++}>
		<Label>Default</Label>
	</Button>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	* :global(.myClass) {
		font-style: italic;
	}
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>