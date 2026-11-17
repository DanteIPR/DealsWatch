<script lang="ts">
	import favicon from '#lib/assets/favicon.svg';
	import type { LayoutProps } from './$types';
	import { page } from '$app/state';
	import { resolve } from '$app/paths';
	import '../app.css';
	let { children }: LayoutProps = $props();
	const pages = [
		{ name: 'Listings', href: '/listings' },
		{ name: 'Rules', href: '/rules' },
		{ name: 'Searches', href: '/searches' },
		{ name: 'Settings', href: '/settings' }
	] as const;
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<nav>
	{#each pages as pageItem (pageItem.href)}
		<a
			href={resolve(pageItem.href)}
			aria-current={page.url.pathname === resolve(pageItem.href) ? 'page' : undefined}
		>
			{pageItem.name}
		</a>
	{/each}
</nav>
{@render children()}

<style>
	nav {
		display: flex; /* lay the links out in a row */
		gap: 1rem; /* space between each link */
		padding: 1rem; /* breathing room inside the bar */
		background: var(--color-surface); /* which variable is for bars/cards? */
	}

	a {
		color: var(--color-muted); /* links not selected: secondary text */
		text-decoration: none; /* remove the underline */
	}

	a[aria-current='page'] {
		color: var(--color-accent); /* the active link stands out */
	}
</style>
