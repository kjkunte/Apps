<template>
  <div class="menu-item" @click="isOpen = !isOpen">
    <a href="#">
     {{ this.severityFor }} 
    </a>
    <svg viewBox="0 0 1030 638" width="10">
      <path d="M1017 68L541 626q-11 12-26 12t-26-12L13 68Q-3 49 6 24.5T39 0h952q24 0 33 24.5t-7 43.5z" fill="#FFF"></path>
    </svg>
    <transition name="fade" appear>
      <div class="sub-menu" v-if="isOpen">
        <div v-for="(item, i) in items" :key="i" class="menu-item">
          <a v-on:click="handleClick(item.id, $event)" v-bind:value="item.id">
              {{ item.title }}
              </a>
        </div>
        <!-- <option v-for="(item, i) in items" :key="i" class="menu-item" v-bind:value="item.id" >
            {{item.title}}
        </option>  -->
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'dropdown',
  props: ['title', 'items'],
  data () {
    return {
      severityFor : this.title,
      isOpen: false
    }
  },
  methods :{
    handleClick(item, event) {
      // alert('Hello');
      alert(event.target.tagName)
        // this.severityFor= item.id
      console.log(item);

      this.$emit("buttonClicked", this.severityFor);
    }
  }
}
</script>

<style>
nav .menu-item svg {
  width: 10px;
  margin-left: 10px;
}
nav .menu-item .sub-menu {
  position: absolute;
  background-color: #222;
  top: calc(100% + 18px);
  left: 50%;
  transform: translateX(-50%);
  width: max-content;
  border-radius: 0px 0px 16px 16px;
}
.fade-enter-active,
.fade-leave-active {
  transition: all .5s ease-out;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>