<!-- Ship.svelte -->
<script>
  export let name;
  export let v;
  const icon = `./images/empty.png`;
  const gradient = `#${v.color}, #${v.color}, #${v.color}`;
  const style = `mask-image: url(${icon}); background-image: linear-gradient(to bottom right, ${gradient});`;
</script>

<div class="flex-box">
  <div class="card-container">
    <div class="gradient-image" {style}></div>
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
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    border: 1px solid black;
  }

  .gradient-image {
    width: 100%;
    height: 100%;
    -webkit-mask-size: cover;
    mask-position: center;
    mask-repeat: no-repeat;
    mask-size: 100%;
    mask-mode: alpha;
  }

  .text-name {
    font-family: "Gotham Light", sans-serif;
    font-size: 16px;
    font-weight: normal;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-bottom: 0px;
    margin-top: 5px;
  }
</style>
