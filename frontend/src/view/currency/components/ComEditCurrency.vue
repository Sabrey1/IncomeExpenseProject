<template>
    <div>
        <Button label="Edit Currency" @click="visible = true" severity="danger" class="w-full md:w-auto" />
        <Dialog v-model:visible="visible" :draggable="false" modal header="Edit Currency" :style="{ width: '22rem' }">
            
            <div class=" mb-4">
                <div class="mb-2">
                    <label for="title" class="font-semibold w-24">Code</label>
                </div>
                <InputText id="title" placeholder="Enter Code" class="flex-auto" fluid autocomplete="off" />
            </div>

            <div class="mb-4">
                <div class="mb-2">
                    <label for="note" class="font-semibold w-24">Description</label>
                </div>
                <Textarea v-model="value" autoResize rows="5" cols="30" fluid />
            </div>

            <div class="flex items-center gap-2">
                <Checkbox v-model="small" binary inputId="small-checkbox" size="small" />
                <Label for="small-checkbox" class="text-sm">Enable</Label>
            </div>
             

            <div class="flex justify-end gap-2 mt-6">
                <Button type="button" label="Cancel" severity="danger" @click="visible = false"></Button>
                <Button type="button" label="Save" @click="visible = false"></Button>
            </div>
        </Dialog>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const visible = ref(false)

</script>