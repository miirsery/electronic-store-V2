<template>
  <header class="header">
    <div
      class="container wrapper flex justify-between border-4 items-center border-b-2 border-gray-100"
    >
      <div class="logo">Logo</div>
      <nav>
        <ul class="relative flex">
          <li class="item mr-4">
            <a class="link" href="/"> Home </a>
          </li>
          <li class="item">
            <a class="link" href="/"> About </a>
          </li>
        </ul>
      </nav>
      <div class="actions">
        <ul class="actions__menu flex">
          <li class="actions__item">
            <a href="/" class="actions__link">Shop</a>
          </li>
          <li class="actions__item ml-4">
            <a href="/" class="actions__link">Favorite</a>
          </li>
        </ul>
      </div>
    </div>
  </header>
</template>

<script>
export default {};
</script>

<style scoped lang="sass">
.logo
  padding: 15px 0

.wrapper
  width: 100%
</style>
