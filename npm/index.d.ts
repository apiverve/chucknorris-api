declare module '@apiverve/chucknorris' {
  export interface chucknorrisOptions {
    api_key: string;
    secure?: boolean;
  }

  /**
   * Describes fields the current plan does not unlock. Locked fields arrive as null
   * in `data`; `locked_fields` names them, using dot paths for nested fields.
   * Absent when the plan unlocks everything.
   */
  export interface PremiumInfo {
    message: string;
    upgrade_url: string;
    locked_fields: string[];
  }

  export interface chucknorrisResponse {
    status: string;
    error: string | null;
    data: ChuckNorrisJokesData;
    code?: number;
    premium?: PremiumInfo;
  }


  interface ChuckNorrisJokesData {
      joke: null | string;
  }

  export default class chucknorrisWrapper {
    constructor(options: chucknorrisOptions);

    execute(callback: (error: any, data: chucknorrisResponse | null) => void): Promise<chucknorrisResponse>;
    execute(query: Record<string, any>, callback: (error: any, data: chucknorrisResponse | null) => void): Promise<chucknorrisResponse>;
    execute(query?: Record<string, any>): Promise<chucknorrisResponse>;
  }
}
