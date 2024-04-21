<script>
	export let name;

	let button1text = "first request";
	let button2text = "second request";

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
	})
</script>

<main>
	<button id='button1'>{button1text}</button>
	<button id='button2'>{button2text}</button>
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