<script>
	export let name;

	let button1text = "first request";
	let button2text = "second request";
	let cards = [];
	let cur_order = 1;
	let more_button_visible = true;

	document.addEventListener("DOMContentLoaded", () => {
		document.getElementById("button1").addEventListener("click", () => {
			fetch("http://localhost:8081/first").then((response) => {
				response.json().then((data) => {
					button1text = data;
				})
			})
		});
		document.getElementById("button2").addEventListener("click", () => {
			fetch("http://localhost:8081/second").then((response) => {
				response.json().then((data) => {
					button2text = data;
				})
			})
		});
		document.getElementById("more").addEventListener("click", () => {
			fetch("https://api.sellershands.ru/api/search/search?sort=anysort&order="+cur_order).then((response) => {
				if (response.status == 206) {
					more_button_visible = false;
				}
				response.json().then((data) => {
					cards = Array.prototype.concat(cards, data);
					cur_order++;
					console.log(cards);
				})
			})
		});
	})
</script>

<main>
	<button id='button1'>{button1text}</button>
	<button id='button2'>{button2text}</button>
	<h1>обьявления</h1>
	{#each cards as card}
		<p>{card.name}</p>
	{/each}
	{#if more_button_visible}
		<button id='more'>показать еще</button>
	{/if}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
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