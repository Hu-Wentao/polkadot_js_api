// Copyright 2017-2023 @polkadot/rpc-provider authors & contributors
// SPDX-License-Identifier: Apache-2.0

import type { Server } from 'mock_socket';

export type Global = typeof globalThis & {
  WebSocket: typeof WebSocket;
  fetch: any;
}

export interface Mock {
  body: Record<string, Record<string, unknown>>;
  requests: number;
  server: Server;
  done: () => Promise<void>;
}

export type MockStateSubscriptionCallback = (error: Error | null, value: any) => void;

export type MockStateSubscriptions = Record<string, {
  callbacks: Record<number, MockStateSubscriptionCallback>;
  lastValue: any;
}>;

export type MockStateDb = Record<string, Uint8Array>;

export type MockStateRequests = Record<string, (db: MockStateDb, params: any[]) => string>;
