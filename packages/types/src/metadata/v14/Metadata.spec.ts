// Copyright 2017-2023 @polkadot/types authors & contributors
// SPDX-License-Identifier: Apache-2.0

import kusamaData from '@polkadot/types_support/metadata/v14/kusama_hex';
import polkadotData from '@polkadot/types_support/metadata/v14/polkadot_hex';
import substrateData from '@polkadot/types_support/metadata/v14/substrate_hex';

import { testMeta } from '../util/testUtil.js';

testMeta(14, {
  kusama: {
    data: kusamaData
  },
  polkadot: {
    data: polkadotData
  },
  substrate: {
    data: substrateData
  }
});
