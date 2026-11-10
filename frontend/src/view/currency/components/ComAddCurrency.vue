<template>
    <div>
        <Button label="Add Currency" @click="visible = true" severity="danger" class="w-full md:w-auto" />
        <Dialog v-model:visible="visible" :draggable="false" modal header="Add Currency" :style="{ width: '22rem' }">
            
            <div class=" mb-4">
                <div class="mb-2">
                    <label for="title" class="font-semibold w-24">Code</label>
                </div>
                <InputText id="title" v-model="data.code" placeholder="Enter Code" class="flex-auto" fluid autocomplete="off" />
            </div>

            <div class="mb-4">
                <div class="mb-2">
                    <label for="note" class="font-semibold w-24">Symbol</label>
                </div>
                <Textarea v-model="data.symbol" autoResize rows="5" cols="30" fluid />
            </div>

            <div class="flex items-center gap-2">
                <Checkbox v-model="data.is_default" binary inputId="default-checkbox" size="small" />
                <label for="default-checkbox" class="font-semibold">Is Default</label>
            </div>
            

            <div class="flex justify-end gap-2 mt-6">
                <Button type="button" label="Cancel" severity="danger" @click="visible = false"></Button>
                <Button type="button" label="Save" @click="saveCurrency"></Button>
            </div>
        </Dialog>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import { useCurrency } from '@/composable/useCurrency'
    const { addCurrency } = useCurrency()
    const visible = ref(false)

    const data = ref({
        code: '',
        symbol: '',
        is_default: false,
    })

    async function saveCurrency() {
        await addCurrency(data.value)
        visible.value = false
    }

</script>