<template>
    <div>
        <Button label="Add Payment Method" @click="visible = true" severity="danger" class="w-full md:w-auto" />
        <Dialog v-model:visible="visible" :draggable="false" modal header="Add Payment Method" :style="{ width: '22rem' }">
            
            <div class=" mb-4">
                <div class="mb-2">
                    <label for="title" class="font-semibold w-24">Name</label>
                </div>
                <InputText id="title" v-model="data.name" placeholder="Enter Name" class="flex-auto" fluid autocomplete="off" />
            </div>

            <div class="flex justify-end gap-2 mt-6">
                <Button type="button" label="Cancel" severity="danger" @click="visible = false"></Button>
                <Button type="button" label="Save" @click="savePaymentMethod"></Button>
            </div>
        </Dialog>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import { usePaymentMethod } from '@/composable/usePaymentMethod'
    const { addPaymentMethod } = usePaymentMethod()
    const visible = ref(false)

    const data = ref({
        name: '',
    })

    async function savePaymentMethod() {
        await addPaymentMethod(data.value)
        visible.value = false
    }

</script>