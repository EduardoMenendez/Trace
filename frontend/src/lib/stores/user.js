// src/lib/stores/user.js
import { writable } from 'svelte/store';

export const user = writable({
    role: '',
    initials: ''
});
