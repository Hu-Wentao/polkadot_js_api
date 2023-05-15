// Copyright 2017-2023 @polkadot/types authors & contributors
// SPDX-License-Identifier: Apache-2.0

import substrateData from '@polkadot/types_support/metadata/v9/substrate_hex';

import { testMeta } from '../util/testUtil.js';

testMeta(9, {
  substrate: {
    data: substrateData
  }
}, false);
