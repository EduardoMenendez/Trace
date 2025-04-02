export { matchers } from './matchers.js';

export const nodes = [
	() => import('./nodes/0'),
	() => import('./nodes/1'),
	() => import('./nodes/2'),
	() => import('./nodes/3'),
	() => import('./nodes/4'),
	() => import('./nodes/5'),
	() => import('./nodes/6'),
	() => import('./nodes/7'),
	() => import('./nodes/8'),
	() => import('./nodes/9'),
	() => import('./nodes/10'),
	() => import('./nodes/11'),
	() => import('./nodes/12'),
	() => import('./nodes/13'),
	() => import('./nodes/14'),
	() => import('./nodes/15'),
	() => import('./nodes/16')
];

export const server_loads = [];

export const dictionary = {
		"/": [4],
		"/auth": [5],
		"/dashboard": [6,[2]],
		"/dashboard/WebTree": [10,[2]],
		"/dashboard/deleted": [7,[2]],
		"/dashboard/folders": [8,[2]],
		"/dashboard/settings": [9,[2]],
		"/[project_id]/ai": [11,[3]],
		"/[project_id]/results": [12,[3]],
		"/[project_id]/tools": [13,[3]],
		"/[project_id]/tools/HttpClient": [14,[3]],
		"/[project_id]/tree": [15,[3]],
		"/[project_id]/tree/WebTree": [16,[3]]
	};

export const hooks = {
	handleError: (({ error }) => { console.error(error) }),
	
	reroute: (() => {}),
	transport: {}
};

export const decoders = Object.fromEntries(Object.entries(hooks.transport).map(([k, v]) => [k, v.decode]));

export const hash = false;

export const decode = (type, value) => decoders[type](value);

export { default as root } from '../root.js';