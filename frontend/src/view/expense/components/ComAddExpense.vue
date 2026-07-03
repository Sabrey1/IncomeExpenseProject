<template>
    <div>
        <Button label="Add Expense" @click="visible = true" severity="danger" class="w-full md:w-auto" />
        <Dialog v-model:visible="visible" :draggable="false" modal header="Add Expense" :style="{ width: '22rem' }">
            
            <div class=" mb-4">
                <div class="mb-2">
                    <label for="title" class="font-semibold w-24">Title</label>
                </div>
                <InputText id="title" placeholder="Enter Title" class="flex-auto" fluid autocomplete="off" />
            </div>

            <div class="mb-4">
                <div class="mb-2">
                    <label for="expense_type" class="font-semibold w-24">Expense Type</label>
                </div>
                <Select v-model="selectedLanguage" :options="languages" fluid optionLabel="label" optionValue="value" placeholder="Select a Expense Type" class="w-full md:w-56" />
            </div>

            <div class="mb-4">
                <div class="mb-2">
                    <label for="expense_type" class="font-semibold w-24">Currency</label>
                </div>
                <Select v-model="selectedLanguage" :options="languages" fluid optionLabel="label" optionValue="value" placeholder="Select a Currency" class="w-full md:w-56" />
            </div>

            <div class="mb-4">
                <div class="mb-2">
                    <label for="expense_type" class="font-semibold w-24">Payment Method</label>
                </div>
                <Select v-model="selectedLanguage" :options="languages" fluid optionLabel="label" optionValue="value" placeholder="Select a Payment Method" class="w-full md:w-56" />
            </div>
            
            <div class="mb-4">
                <div class="mb-2">
                    <label for="amount" class="font-semibold w-24">Amount</label>
                </div>
                <InputText id="amount" placeholder="Enter Amount" class="flex-auto" fluid autocomplete="off" />
            </div>

            <div class="mb-4">
                <div class="mb-2">
                    <label for="note" class="font-semibold w-24">Note</label>
                </div>
                <Textarea v-model="value" autoResize rows="5" cols="30" fluid />
            </div>


            <div class="flex justify-end gap-2">
                <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
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