<!-- CounterComponent.vue -->
<template>
  <div>
    <button @click="increment">{{ count }}</button>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup(_, context) {
    const count = ref(0);
    const increment = () => {
      count.value++;
      if (count.value === 10) {
        context.emit('reachedTen'); // 发出 reachedTen 事件
      }
    };
    return {
      count,
      increment
    };
  }
};
</script>
