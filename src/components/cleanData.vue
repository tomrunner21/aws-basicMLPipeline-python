<template>

<div class="container py-5">
    <header class="text-white text-center">
        <h1 class="display-4">ML model Pipeline:</h1>
    </header>

    <div class="row py-4">
        <div class="col-lg-6 mx-auto">
            <p class="font-italic text-white text-center">Insert the data file (.csv only) below:</p>
                <input id="fileInput" type="file">
            </div>
        </div>
        <div>
            <button @click="runPythonProgram">Run Python Program</button>
            <div v-if="result !== null">Result: {{ result }}</div>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            result: null
        };
    },
    methods: {
        async runPythonProgram() {
        try {
                // Make a request to the Python program using Node.js child_process module
                const { exec } = require('child_process');
                exec('python ../lambdas/aiPipeline.py', (error, stdout, stderr) => {
                if (error) {
                    console.error('Error running Python program:', error);
                    return;
                }
                this.result = stdout.trim();
            });
        } catch (error) {
            console.error('Error running Python program:', error);
        }
        }
    }
    };
</script>
  