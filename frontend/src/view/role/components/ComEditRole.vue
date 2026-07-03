<template>
    <div>
        <Button label="Edit Role" @click="visible = true" severity="danger" class="w-full md:w-auto" />
        <Dialog v-model:visible="visible" :draggable="false" modal header="Edit Role" :style="{ width: '22rem' }">
            
            <div class=" mb-4">
                <div class="mb-2">
                    <label for="title" class="font-semibold w-24">Role Name</label>
                </div>
                <InputText id="title" placeholder="Enter Role Name" class="flex-auto" fluid autocomplete="off" />
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


const selectedLanguage = ref(null);
const languages = ref([
    { label: 'English', value: 'en' },
    { label: 'Deutsch', value: 'de' },
    { label: 'Español', value: 'es' },
    { label: 'Français', value: 'fr' },
    { label: 'Italiano', value: 'it' },
    { label: 'Türkçe', value: 'tr' },
    { label: '日本語', value: 'ja' },
    { label: '中文', value: 'zh' }
]);
</script>