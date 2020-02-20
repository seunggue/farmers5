<template>
  <div class="SNS">
    <section class="blog-post-area">
      <div>
        <img src="img/snsmain.png" style="width:100%;">
    </div>
      <div class ="container">
        <div class = "row">
            <Com_Sns_Right/>
            <Com_Sns_Left/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Com_Sns_Left from '@/components/Com_Sns_Left.vue'
import Com_Sns_Right from '@/components/Com_Sns_Right.vue'

export default {
  name: 'SNS',
  components: {
    Com_Sns_Left,
    Com_Sns_Right,
  }
}
</script>