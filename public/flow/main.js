Object.values(config.steps)
function* mount(steps){
    nextStepsKeys = [null]
    while(nextStepsKeys.length){
        nextSteps = steps.filter(step=>nextStepsKeys.includes(step.dependsOn))
        nextStepsKeys = nextSteps.map(({key})=>key)
        nextSteps.length && (yield nextSteps)
    }
} 