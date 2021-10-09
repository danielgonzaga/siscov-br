import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MinasGeraisComponent } from './minas-gerais.component';

describe('MinasGeraisComponent', () => {
  let component: MinasGeraisComponent;
  let fixture: ComponentFixture<MinasGeraisComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MinasGeraisComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MinasGeraisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
