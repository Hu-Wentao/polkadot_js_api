// Copyright 2017-2023 @polkadot/api authors & contributors
// SPDX-License-Identifier: Apache-2.0

import { packageInfo as deriveInfo } from '@polkadot/api_derive/packageInfo';
import { packageInfo as coreInfo } from '@polkadot/rpc_core/packageInfo';
import { packageInfo as providerInfo } from '@polkadot/rpc_provider/packageInfo';
import { packageInfo as typesInfo } from '@polkadot/types/packageInfo';
import { packageInfo as knownInfo } from '@polkadot/types_known/packageInfo';

export default [deriveInfo, coreInfo, providerInfo, typesInfo, knownInfo];
