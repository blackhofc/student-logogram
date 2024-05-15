<script>
  import { onMount } from "svelte";
  import { Link } from "svelte-routing";

  // Import Utils
  import { loadStudents, describeStudent, extractParams } from "./utils/utils";

  // Import componenets
  import Student from "./Component/SmallGram.svelte";
  import SmokeEffect from "./Component/Effects/Smoke.svelte";
  import PopAbout from "./Component/Popup/About.svelte";

  // Retrieve the id parameter from the URL
  const params = extractParams(window);
  console.log(params.id);

  // Variables
  let isAboutVisible = false;
  let selectedStudent = null;
  let style = "";
  let students = loadStudents();

  // Define a function to handle the custom event
  function handleStudentClick(event) {
    console.log("event", event);
    // Access the student data from the event detail
    if (event) {
      const selectedLogogram = event.detail;
      selectedStudent = selectedLogogram.detail;
    }

    students = loadStudents(selectedStudent.id);

    console.log("Student clicked in App:", selectedStudent);
    style = `mask-image: url(${selectedStudent.symbolBig}); background-image: linear-gradient(135deg, ${selectedStudent.gradient});`;
  }

  // On website mounted
  onMount(() => {
    console.log(students);
    selectedStudent = students.find(
      (student) => student.id === parseInt(params.id)
    );
    console.log(selectedStudent);

    handleStudentClick();
  });
</script>

<Link
  to="/"
  class="back"
  style="display: flex; position: absolute; margin-top: 25px; margin-left: 16px"
>
  <img
    class="back-img"
    src={"/images/arrow_back.png"}
    style="max-width: 150px; z-index: 1000"
    alt=""
  />
</Link>

<button
  class="about-button"
  on:click={function handle() {
    isAboutVisible = !isAboutVisible;
  }}
>
  <img src="/images/about.png" alt="About" />
</button>

<div class="page">
  <div class="row-container">
    <div class="logograms-container">
      {#each students as student}
        <Student {student} on:studentClicked={handleStudentClick} />
      {/each}
    </div>

    <div class="current-logogram-container">
      <div class="gradient-image" {style}></div>
    </div>

    <div class="data-container">
      <div class="text-title" style="font-size: 35px; color: #2E302F; ">
        {selectedStudent?.id}th Logogram
      </div>

      <div class="description-container">
        {#each describeStudent(selectedStudent) as entity}
          {#if entity.type === "word"}
            <div class="text-sub" style="color: #2E302F; ">
              {entity.value}
            </div>
          {:else}
            <div
              class="mini-gram"
              style={`mask-image: url(/images/translator/${entity.value}.png);`}
            ></div>
          {/if}
        {/each}
      </div>
    </div>
  </div>
</div>
<SmokeEffect />

<PopAbout
  visible={isAboutVisible}
  onClose={function () {
    isAboutVisible = !isAboutVisible;
  }}
/>

<style>
  .page {
    display: flex;
    position: fixed;
    max-width: 100vw;
    max-height: 100vh;
    height: 100%;
    width: auto;
    flex-direction: row;
    align-items: center;
    z-index: 1500;
  }

  .row-container {
    display: flex;
    position: absolute;
    max-width: 100vw;
    max-height: 80vh;
    height: 100%;
    width: 100vw;
    flex-direction: row;
    align-items: center;
  }

  .logograms-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
    justify-items: center;
    width: 100%;
    height: 100%;
    max-width: 25%;
    overflow-y: auto;
    background-color: #0000008a;
    margin-left: 16px;
    padding: 16px;
    border-radius: 10px;
  }

  .current-logogram-container {
    display: flex;
    position: relative;
    width: 100%;
    height: 100%;
    margin-left: 32px;
    margin-right: 32px;
    animation: smooth 5s infinite alternate ease-in-out;
    align-items: center;
  }

  .data-container {
    display: flex;
    position: relative;
    height: 100%;
    width: 100%;
    max-width: 25%;
    flex-direction: column;
    flex-wrap: nowrap;
    overflow-y: auto;
  }

  .gradient-image {
    width: 100%;
    height: 110%;
    -webkit-mask-size: cover;
    mask-position: center;
    mask-repeat: no-repeat;
    mask-size: 100%;
    mask-mode: alpha;
    color: transparent;
    background-size: 300% 300%;
    animation: glowing 2s ease infinite;
    margin-top: 10px;
  }

  @keyframes glowing {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }

  @keyframes animateGradient {
    0% {
      background-position: 200% 50%;
    }
    50% {
      background-position: 0% 50%;
    }
    100% {
      background-position: -200% 50%;
    }
  }

  @keyframes smooth {
    0% {
      transform: translateX(-5px) scale(1) rotate(-2deg);
    }
    50% {
      transform: translateX(5px) scale(1.05) rotate(1deg);
    }
    100% {
      transform: translateX(-5px) scale(1) rotate(-2deg);
    }
  }

  .back-img:hover {
    animation: expand 0.1s ease-in-out forwards;
  }

  .text-title {
    font-family: "Gotham Light", sans-serif;
    font-size: 50px;
    color: #444444;
  }

  .description-container {
    display: flex;
    position: relative;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    margin-right: 32px;
  }

  .text-sub {
    font-family: "Gotham Light", sans-serif;
    font-size: 30px;
    color: #797979;
    margin-right: 7px;
    z-index: 1200;
  }

  .mini-gram {
    width: 100px;
    height: 100px;
    background-color: black;
    mask-size: 100%;
    margin-bottom: -25px;
    margin-top: -25px;
    margin-left: -12.5px;
    margin-right: -12.5px;
    z-index: 1000;
  }

  .about-button {
    border: none;
    background: none;
    z-index: 3000;
    position: fixed;
    bottom: 20px;
    right: 20px;
    cursor: pointer;
  }

  .about-button img {
    display: block;
    width: 70px;
    height: auto;
  }

  .about-button:hover {
    animation: expand 0.1s ease-in-out forwards;
  }

  @keyframes expand {
    0% {
      transform: scale(1);
    }
    100% {
      transform: scale(1.2);
    }
  }

  /* width */
  ::-webkit-scrollbar {
    height: 10px;
    width: 6px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 1px #808080;
    border-radius: 0px;
    background-color: #212224;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #b3b3b3;
    border-radius: 0px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #808080;
  }

  :global(body) {
    background-image: url("/images/background.jpg");
    background-attachment: fixed;
    height: 100%;
    width: 100%;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
  }
</style>
