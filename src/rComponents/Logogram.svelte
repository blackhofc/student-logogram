<script>
  import { createEventDispatcher } from "svelte";

  export let student;

  let styles = {
    mask: `mask-image: url(${student.symbol}); background-image: linear-gradient(to bottom right, #FDFDFD, #FDFDFD);`,
    card: "background: #0000008a;",
  };

  const dispatch = createEventDispatcher();

  // Reactive statement to update styles when student.selected changes
  $: {
    if (student.selected) {
      styles.mask = `mask-image: url(${student.symbol}); background-image: linear-gradient(to bottom right, #212224, #212224);`;
      styles.card = "background: #FDFDFD;";
    } else {
      styles.mask = `mask-image: url(${student.symbol}); background-image: linear-gradient(to bottom right, #FDFDFD, #FDFDFD);`;
      styles.card = "background: #0000008a;";
    }
  }

  // Function to handle click event
  function handleClick() {
    dispatch("studentClicked", { detail: student });
  }

  function handleMouseOver() {
    console.log("HOVER", student.name);
  }

  function handleMouseLeave() {
    console.log("LEAVED", student.name);
  }

  function handleFocus() {
    handleMouseOver();
  }
</script>

<div
  class="flex-box"
  on:click={handleClick}
  on:keydown={null}
  tabindex="0"
  role="button"
  aria-label={`Click to view details of ${student.name}`}
  on:mouseover={handleMouseOver}
  on:mouseleave={handleMouseLeave}
  on:focus={handleFocus}
>
  <div class="card-container" style={styles.card}>
    <div class="gradient-image" style={styles.mask}></div>
  </div>
</div>

<style>
  .flex-box {
    margin: 4px;
    width: 100px;
    height: 100px;
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  .card-container {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    position: relative;
    border: 0px solid black;
    padding-bottom: 1px;
  }

  .gradient-image {
    width: 100%;
    height: 100%;
    mask-size: 100%;
  }
</style>
