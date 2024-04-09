<script>
  import { onMount } from "svelte";

  // Import data
  import students from "./students.json";
  import symbols from "./translations.json";

  // Import componenets
  import Student from "./components/Student.svelte";
  import Variable from "./components/Variable.svelte";
  import Container from "./components/Container.svelte";
  import Music from "./components/Music.svelte";
  import Popup from "./components/Popup.svelte";
  let isPopupVisible = false;
  let slectedStudent = null;

  function togglePopup() {
    isPopupVisible = !isPopupVisible;
  }

  function describe(student) {
    const name = student.name.split(" ")[0];
    const gender = student.gender;
    const age = student.age;
    const genres = student.music_genres.join(", ");
    const sports = student.fav_sports.join(", ");
    const languages = student.languages.join(", ");

    return `${name} es ${gender}, tiene ${age} años, escucha genero ${genres}, le gusta mirar ${sports} y habla en ${languages}.`;
  }

  // Define a function to handle the custom event
  function handleStudentClick(event) {
    // Access the student data from the event detail
    const selectedLogogram = event.detail;
    slectedStudent = selectedLogogram.detail;
    console.log("Student clicked in App:", selectedLogogram);
    togglePopup();
    // Perform any action you want when a student is clicked
  }

  const variables = {
    gender: { title: "Género", description: "Ubicado a 90°" },
    /*age: {
      title: "Age",
      description: "Gender symbol size",
    }, */
    music_genres: {
      title: "Intereses Musicales",
      description: "Gradiente del logograma",
    },
    fav_sports: {
      title: "Deportes Favoritos",
      description: "Ubicados a 135°, 180°, 225°",
    },
    languages: { title: "Idiomas", description: "Ubicados a 0°, 45°, 315°" },
  };

  // Load student nodes with its values
  const parsedStudents = [];

  students.forEach((person) => {
    const { id, name, age, gender, music_genres, fav_sports } = person;

    const defaultColor = "#000"; // Default color if music genres are not available
    let colors;

    if (music_genres.length === 0) {
      // If no music genres are available, duplicate the default color
      colors = [defaultColor, defaultColor];
    } else if (music_genres.length === 1) {
      // If there's only one music genre, duplicate the unique color
      colors = [music_genres[0], music_genres[0]].map(
        (genre) =>
          `#${
            symbols["music_genres"][genre]?.color ||
            symbols["music_genres"]["Otros"].color
          }`
      );
    } else {
      colors = music_genres.map(
        (genre) =>
          `#${
            symbols["music_genres"][genre]?.color ||
            symbols["music_genres"]["Otros"].color
          }`
      );
    }

    parsedStudents.push({
      ...person,
      symbol: `../../public/images/logograms/${id}.png`,
      gradient: colors.join(", "),
    });
  });

  // TODO: on click student opens a right view with student name, age interest with its respective icons
  // On website mounted
  onMount(() => {});
</script>

<div class="head-container">
  <div class="text-title" style="font-size: 65px; margin-top: 32px;">
    Student Logogram
  </div>
  <div style="margin-top: 15px;" class="text-sub">
    La representación en logograma de los intereses de un estudiante en el
    lenguaje alien
  </div>
  <a
    class="text-sub"
    style=" text-decoration: underline; text-underline-offset: 5px"
    href="https://creativechair.org/stephen-wolfram/"
    target="_blank"
  >
    (Referencia de Inspiración)
  </a>
</div>

<div class="variables-container">
  {#each Object.entries(variables) as [key, variable]}
    <Variable {variable} />

    <div class="row-container">
      <div class="container">
        {#if key === "music_genres"}
          {#each Object.entries(symbols[key]) as [name, symbol]}
            <Music {name} v={symbol} />
          {/each}
        {:else}
          {#each Object.entries(symbols[key]) as [name, symbol]}
            <Container {name} {symbol} />
          {/each}
        {/if}
      </div>
    </div>
  {/each}
</div>

<div class="logograms-container">
  {#each parsedStudents as student}
    <Student {student} on:studentClicked={handleStudentClick} />
  {/each}
</div>

<Popup visible={isPopupVisible} onClose={togglePopup}>
  <h2 class="text-title">{slectedStudent.name}</h2>
  <p class="text-sub">{describe(slectedStudent)}</p>
  <Student student={slectedStudent} />
</Popup>

<style>
  .head-container {
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: column;
    flex-wrap: wrap;
    margin: 15px;
    justify-content: space-between;
  }

  .variables-container {
    display: flex;
    position: relative;
    align-items: start;
    flex-direction: column;
    flex-wrap: wrap;
    padding-left: 32px;
    padding-right: 32px;
    align-items: center;
  }

  .row-container {
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: row;
    max-width: 80%;
    overflow-x: auto;
  }

  .container {
    display: flex;
    align-items: start;
    height: auto;
    flex-wrap: nowrap; /* Prevent wrapping onto multiple lines */
    flex-direction: row;
    margin-bottom: 8px;
  }

  .logograms-container {
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
    margin: 20px;
  }

  :global(body) {
    background-color: white;
    height: 100vh;
    width: 100%;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
  }

  .text-title {
    font-family: "Gotham Light", sans-serif;
    font-size: 50px;
    color: #444444;
  }

  .text-sub {
    font-family: "Gotham Light", sans-serif;
    font-size: 16px;
    color: #797979;
    margin-left: 4px;
  }

  /* width */
  ::-webkit-scrollbar {
    height: 10px;
    width: 2px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 1px grey;
    border-radius: 0px;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #969696;
    border-radius: 0px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #141414;
  }
</style>
