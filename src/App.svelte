<script>
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

	function handleSubmit() {
		var files = document.forms['formName']['files'].files;
		console.log(files);
		console.log(document.forms['formName']['cardId'].value);
		console.log(document.forms['formName']['authToken'].value);
		var counter = 4;
		Array.prototype.forEach.call(files, function (file) {
			console.log("post index "+Math.abs(counter-5));
			console.log(file);
			let formData = new FormData();
			formData.append('file', file);
			fetch("https://api.sellershands.ru/api/cards/card/"+document.forms['formName']['cardId'].value+"/photo?" + new URLSearchParams({ authToken: document.forms['formName']['authToken'].value, number: Math.abs(counter-5) }).toString(), {
				method: "POST",
				mode: "no-cors",
				body: formData
			}).then((res) => {
				console.log(res);
			})
			counter--;
		})
		for (let i = 4; i >= Math.abs(counter-5); i--) {
			console.log("delete index "+i);
				fetch("https://api.sellershands.ru/api/cards/card/"+document.forms['formName']['cardId'].value+"/photo?"+ new URLSearchParams({ authToken: document.forms['formName']['authToken'].value, number: i }).toString(), {
					method: "DELETE"
				}).then((res) => {
					console.log(res);
				}).catch((e) => {
					
				})
		}
		return false;
	}
</script>

<main>
	<button id='button1'>{button1text}</button>
	<button id='button2'>{button2text}</button>
	<form on:submit={handleSubmit} formName="formName" name="formName" onsubmit="return false">
		<input type='text' placeholder="authToken" name="authToken">
		<input type='text' placeholder="cardId" name="cardId">
		<input type='file' multiple name="files">
		<button>send</button>
	</form>
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

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>