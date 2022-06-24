import { Test, TestingModule } from '@nestjs/testing';
import { ObdController } from './obd.controller';

describe('ObdController', () => {
  let controller: ObdController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [ObdController],
    }).compile();

    controller = module.get<ObdController>(ObdController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
