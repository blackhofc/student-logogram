<!-- Ship.svelte -->
<script>
  export let symbol;
  export let name;
  const icon = `../../public/images/translator/${symbol.id}.png`;
</script>

<div class="flex-box">
  <div class="card-container">
    <img class="card-container-hetapod" src={icon} alt="" />
  </div>
  <p class="text-name">{name}</p>
</div>

<style>
  .flex-box {
    margin: 8px;
    width: 150px;
    height: 150px;
    background-color: #ffffff;
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  .card-container {
    width: 100%;
    height: 100%;
    /*background: linear-gradient(to bottom right, #ff9999, #66ccff, #99ff99); */
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    position: relative;
    border: 1px solid black;
  }

  .card-container-hetapod {
    max-width: 100%;
    padding-left: 8px;
    padding-right: 8px;
    position: absolute;
  }

  .text-name {
    font-family: "Gotham Light", sans-serif; /* Fallback to sans-serif if Gotham Light is not available */
    font-size: 16px;
    font-weight: normal; /* Make sure to set font-weight to normal if you're using a specific font weight */
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-bottom: 0px;
    margin-top: 5px;
  }
</style>
