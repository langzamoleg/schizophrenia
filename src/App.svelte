<script>
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

	function handleSubmit() {
		var files = document.forms['formName']['files'].files;
		console.log(files);
		console.log(document.forms['formName']['cardId'].value);
		console.log(document.forms['formName']['authToken'].value);
		var counter = 4;
		Array.prototype.forEach.call(files, function (file) {
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
		for (let i = 0; i < counter; i++) {
			fetch("https://api.sellershands.ru/api/cards/card/"+document.forms['formName']['cardId'].value+"/photo?"+ new URLSearchParams({ authToken: document.forms['formName']['authToken'].value, number: Math.abs(counter-5) }).toString(), {
				method: "DELETE"
			}).then((res) => {
				console.log(res);
			})
			counter--;
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