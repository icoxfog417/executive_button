<template>
  <v-layout column justify-center align-center>
    <div class="text-center">
      <div class="display-3">
        エグゼクティブになった!
      </div>
      <hr />
      <br />
      <v-card class="mx-auto" max-width="400">
        <v-img src="/after.png"></v-img>
        <v-card-title>
          {{ executive.filer_name }} <br />
          (証券コード: {{ secCode }})
        </v-card-title>
        <v-card-title>{{ salary }}円ゲット!</v-card-title>
      </v-card>
    </div>
  </v-layout>
</template>

<script>
export default {
  async asyncData(ctx) {
    // 1944 is maximum number of company
    const index = Math.floor(Math.random() * Math.floor(1944));
    return {
      executive: await ctx.app.$executiveRepository.get(index).catch(error => {
        console.log(error);
        return {
          executive: {}
        };
      })
    };
  },
  data() {
    return {
      executive: {}
    };
  },
  computed: {
    secCode() {
      return this.executive.sec_code.slice(0, 4);
    },
    salary() {
      const salary = Math.round(this.executive.amount / this.executive.number);
      return salary.toLocaleString();
    }
  },
  methods: {
    async beExecutive() {
      const result = await this.$executiveRepository.create({
        title: "clicked"
      });
    }
  }
};
</script>
