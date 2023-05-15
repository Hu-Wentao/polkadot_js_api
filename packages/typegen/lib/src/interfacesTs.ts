// Copyright 2017-2023 @polkadot/typegen authors & contributors
// SPDX-License-Identifier: Apache-2.0

import type { HexString } from '@polkadot/util/types';

import kusama from '@polkadot/types_support/metadata/static_kusama';
import polkadot from '@polkadot/types_support/metadata/static_polkadot';
import substrate from '@polkadot/types_support/metadata/static_substrate';

import { generateDefaultConsts, generateDefaultErrors, generateDefaultEvents, generateDefaultInterface, generateDefaultLookup, generateDefaultQuery, generateDefaultRpc, generateDefaultRuntime, generateDefaultTsDef, generateDefaultTx } from './generate/index.js';

const BASE = 'packages/api-augment/src';
const METAS = Object.entries<HexString>({ kusama, polkadot, substrate });

export function main (): void {
  generateDefaultInterface();
  generateDefaultLookup();
  generateDefaultRpc();
  generateDefaultTsDef();

  for (const [name, staticMeta] of METAS) {
    console.log();
    console.log(`*** Generating for ${name}`);

    generateDefaultConsts(`${BASE}/${name}/consts.ts`, staticMeta);
    generateDefaultErrors(`${BASE}/${name}/errors.ts`, staticMeta);
    generateDefaultEvents(`${BASE}/${name}/events.ts`, staticMeta);
    generateDefaultQuery(`${BASE}/${name}/query.ts`, staticMeta);
    generateDefaultRuntime(`${BASE}/${name}/runtime.ts`, staticMeta);
    generateDefaultTx(`${BASE}/${name}/tx.ts`, staticMeta);
  }
}
