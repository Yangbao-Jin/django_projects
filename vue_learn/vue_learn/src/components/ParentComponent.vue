<!-- ParentComponent.vue -->
<template>
    <div>
      <CounterComponent @reachedTen="handleReachedTen" />
    </div>
  </template>
  
  <script>
  import CounterComponent from './CounterComponent.vue';
  
  export default {
    components: {
      CounterComponent
    },
    methods: {
      handleReachedTen() {
        console.log('The count in CounterComponent reached 10!');
        // 这里可以执行其他操作，例如显示一个通知、更新其他数据等。
      }
    }
  };
  </script>
  