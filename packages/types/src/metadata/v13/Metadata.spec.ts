// Copyright 2017-2023 @polkadot/types authors & contributors
// SPDX-License-Identifier: Apache-2.0

import kusamaData from '@polkadot/types_support/metadata/v13/kusama_hex';
import polkadotData from '@polkadot/types_support/metadata/v13/polkadot_hex';
import substrateData from '@polkadot/types_support/metadata/v13/substrate_hex';

import { testMeta } from '../util/testUtil.js';

testMeta(13, {
  kusama: {
    data: kusamaData,
    fails: [
      // RawSolution has 24 entries
      'SignedSubmissionOf'
    ]
  },
  polkadot: {
    data: polkadotData
  },
  substrate: {
    data: substrateData
  }
});
