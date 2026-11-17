<script lang="ts">
	import favicon from '#lib/assets/favicon.svg';
	import type { LayoutProps } from './$types';
	import { page } from '$app/state';
	import { resolve } from '$app/paths';
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
