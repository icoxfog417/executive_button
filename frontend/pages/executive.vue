<template>
  <v-layout column justify-center align-center>
    <div class="text-center">
      <div class="display-3">エグゼクティブになった!</div>
      <hr />
      <br />
      <v-card class="mx-auto" max-width="400">
        <v-img src="/after.png"></v-img>
        <v-card-title>
          {{ executive.filer_name }}
        </v-card-title>
        <v-card-subtitle class="pb-0">
          {{ executive.edinet_code }}
        </v-card-subtitle>
      </v-card>
    </div>
  </v-layout>
</template>

<script>
export default {
  async asyncData(ctx) {
    return {
      executive: await ctx.app.$executiveRepository.get(1).catch(error => {
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
  methods: {
    async beExecutive() {
      const result = await this.$executiveRepository.create({
        title: "clicked"
      });
    }
  }
};
</script>
