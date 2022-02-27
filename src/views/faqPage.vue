<template>
  <div>
    <router-link to="/" class="actions__link text-gray-800 bold mb-4 block">Домой</router-link>
    <div class="collapse">
      <el-collapse v-model="activeName" accordion>
        <el-collapse-item title="Title1" name="1">
          <div>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorem doloremque eos, ipsam minus pariatur
            quas quia. Alias aspernatur consequuntur dicta, dignissimos, ea modi nostrum officiis provident quaerat
            quisquam sint suscipit!
          </div>
        </el-collapse-item>
        <el-collapse-item title="Title2" name="2">
          <div>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorem doloremque eos, ipsam minus pariatur
            quas quia. Alias aspernatur consequuntur dicta, dignissimos, ea modi nostrum officiis provident quaerat
            quisquam sint suscipit!
          </div>
        </el-collapse-item>
        <el-collapse-item title="Title3" name="3">
          <div>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorem doloremque eos, ipsam minus pariatur
            quas quia. Alias aspernatur consequuntur dicta, dignissimos, ea modi nostrum officiis provident quaerat
            quisquam sint suscipit!
          </div>
        </el-collapse-item>
        <el-collapse-item title="Title4" name="4">
          <div>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolorem doloremque eos, ipsam minus pariatur
            quas quia. Alias aspernatur consequuntur dicta, dignissimos, ea modi nostrum officiis provident quaerat
            quisquam sint suscipit!
          </div>
        </el-collapse-item>
      </el-collapse>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";

const activeName = ref("");
</script>

<style scoped lang="sass">
.collapse
  max-width: 30%
</style>