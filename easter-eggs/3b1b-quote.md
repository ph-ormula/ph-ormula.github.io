---
layout: default
title: 3Blue1Brown Quote
permalink: /easter-eggs/3b1b-quote/
---

<audio id="3b1b-quote" controls>
	<source src="/easter-eggs/3b1b-quote.mp3" type="audio/mpeg">
</audio>

<script>
	const playAudio = () => {
		const audio = document.getElementById('3b1b-quote');
		audio.play().catch(err => console.log("Playback blocked:", err));

		// Clean up: Remove both listeners once the audio starts
		document.removeEventListener('click', playAudio);
		document.removeEventListener('keydown', playAudio);
	};

	// Listen for both mouse clicks and keyboard presses
	document.addEventListener('click', playAudio);
	document.addEventListener('keydown', playAudio);
</script>
